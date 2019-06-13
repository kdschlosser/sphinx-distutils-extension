# -*- coding: utf-8 -*-

import sys

if 'setuptools' in sys.modules:
    from setuptools import Command

else:
    from distutils.cmd import Command

import os
import sys
import traceback
import shutil


class build_docs(Command):
    description = 'Build Documentation.'

    user_options = [
        (
            'builder-name=',
            'b',
            "compiler to use. Can be one of the following - html, dirhtml, "
            "singlehtml, htmlhelp, qthelp, devhelp, epub, applehelp, latex, "
            "man, texinfo, text, gettext, doctest, linkcheck, xml, pseudoxml\n"
            "the following builders are only available if make mode is being "
            "used - latexpdf, info\n default is html"
        ),
        (
            'make-mode',
            'M',
            "Uses the Sphinx make_mode module, which provides the same build "
            "functionality as a default Makefile or Make.bat. In addition to "
            "all Sphinx Builders, the following build pipelines are "
            "available: latexpdf, info"
        ),
        (
            'all-output',
            'a',
            "If given, always write all output files. The default is to only "
            "write output files for new and changed source files. (This may "
            "not apply to all builders."
        ),
        (
            'no-saved-environment',
            'E',
            "Don’t use a saved environment (the structure caching all "
            "cross-references), but rebuild it completely. The default is to "
            "only read and parse source files that are new or have changed "
            "since the last run."
        ),
        (
            'tag=',
            't',
            "Define the tag tag. This is relevant for only directives that "
            "only include their content if this tag is set."
        ),
        (
            'doctree-path=',
            'd',
            "Since Sphinx has to read and parse all source files before it "
            "can write an output file, the parsed source files are cached as "
            "'doctree pickles'. Normally, these files are put in a directory "
            "called .doctrees under the build directory; with this option you "
            "can select a different cache directory (the doctrees can be "
            "shared between all builders)."
        ),
        (
            'num-processes',
            'j',
            "Distribute the build over N processes in parallel, to make "
            "building on multiprocessor machines more effective. Note that "
            "not all parts and not all builders of Sphinx can be "
            "parallelized. If auto argument is given, Sphinx uses the number "
            "of CPU cores. default is auto"
        ),
        (
            'config-path=',
            'c',
            "Don’t look for the conf.py in the source directory, but use the "
            "given configuration directory instead. Note that various other "
            "files and paths given by configuration values are expected to be "
            "relative to the configuration directory, so they will have to be "
            "present at this location too."
        ),
        (
            'no-config',
            'C',
            "Don’t look for a configuration file; only take options via "
            "the -D option."
        ),
        (
            'nit-picky',
            'n',
            "Run in nit-picky mode. Currently, this generates warnings for "
            "all missing references. See the config value nitpick_ignore for "
            "a way to exclude some references as 'known missing'."
        ),
        (
            'no-color',
            'N',
            "Do not emit colored output."
        ),
        (
            'quiet',
            'q',
            "Do not output anything on standard output, only write warnings "
            "and errors to standard error."
        ),
        (
            'only-errors',
            'Q',
            "Do not output anything on standard output, also suppress "
            "warnings. Only errors are written to standard error."
        ),
        (
            'error-log=',
            'w',
            "Write warnings (and errors) to the given file, in addition to "
            "standard error."
        ),
        (
            'warnings-are-errors',
            'W',
            "Turn warnings into errors. This means that the build stops at "
            "the first warning and sphinx-build exits with exit status 1."
        ),
        (
            'keep-going',
            None,
            "With -W option, keep going processing when getting warnings to "
            "the end of build, and sphinx-build exits with exit status 1."
        ),
        (
            'full-traceback',
            'T',
            "Display the full traceback when an unhandled exception occurs. "
            "Otherwise, only a summary is displayed and the traceback "
            "information is saved to a file for further analysis."
        ),
        (
            'output-path=',
            None,
            'Output path. defaults to {source path}/_build'
        ),
        (
            'source-path=',
            None,
            'Path to the source files. defaults to {current path}/docs'
        ),
        (
            'config-overrides=',
            'D',
            'Override a configuration value set in the conf.py file.\n'
            'The value must be a number, string, list or dictionary value.\n'
            'We are not able to directly duplicate the command line syntax '
            'from Sphinx. There are some changes needed to be made in order '
            'to get this parameter to work properly.\n'
            'each entry will be setting=value separated by a semicolon\n'
            'setting=value;setting=value;setting=value\n'
            'For lists, html_theme_path=path1,path2.\n'
            'For dictionary values, supply the setting name and key like '
            'this: latex_elements.docclass=scrartcl.\n'
            'For boolean values, use 0 or 1 as the value.'
        ),
        (
            'html-values=',
            'A',
            'Make the name assigned to value in the HTML templates.\n'
            'We are not able to directly duplicate the command line syntax '
            'from Sphinx. There are some changes needed to be made in order '
            'to get this parameter to work properly.\n'
            'each entry will be setting=value separated by a semicolon\n'
            'setting=value;setting=value;setting=value\n'
        ),
    ]

    boolean_options = [
        'full-traceback'
        'keep-going',
        'warnings-are-errors',
        'only-errors',
        'quiet',
        'no-color',
        'nit-picky',
        'no-config',
        'no-saved-environment',
        'all-output',
        'make-mode'
    ]

    sphinx_conf = None

    def initialize_options(self):

        try:
            import sphinx
        except ImportError:
            raise RuntimeError(
                'Sphinx needs to be installed in order to use '
                'this extension.\n'
                'If using setuptools you can add Sphinx to the setup_requires'
                'parameter of setuptools.setup.\n'
                'Or it has to be installed before running your setup program'
            )
        self.html_values = ''
        self.config_overrides = ''
        self.source_path = '/docs'
        self.output_path = None
        self.full_traceback = False
        self.builder_name = 'html'
        self.make_mode = False
        self.all_output = False
        self.no_saved_environment = False
        self.tag = None
        self.doctree_path = None
        self.num_processes = 'auto'
        self.config_path = None
        self.no_config = False
        self.keep_going = False
        self.warnings_are_errors = False
        self.error_log = None
        self.only_errors = False
        self.quiet = False
        self.no_color = False
        self.nit_picky = False
        self.config_backup = None

    def finalize_options(self):
        flatten = lambda l: [item for sublist in l for item in sublist]

        if self.html_values:
            self.html_values = flatten(
                ['-A', item] for item in self.html_values.split(';')
            )
        else:
            self.html_values = []

        if self.config_overrides:
            self.config_overrides = flatten(
                ['-D', item] for item in self.config_overrides.split(';')
            )
        else:
            self.config_overrides = []

        if self.full_traceback:
            self.full_traceback = ['-T']
        else:
            self.full_traceback = []

        if self.make_mode:
            self.builder_name = ['-M', self.builder_name]

        else:
            self.builder_name = ['-b', self.builder_name]

        if self.all_output:
            self.all_output = ['-a']
        else:
            self.all_output = []

        if self.no_saved_environment:
            self.no_saved_environment = ['-E']
        else:
            self.no_saved_environment = []

        if self.tag is None:
            self.tag = []
        else:
            self.tag = ['-t', self.tag]

        if self.doctree_path is None:
            self.doctree_path = []
        else:
            self.doctree_path = ['-d', self.doctree_path]

        self.num_processes = ['-j', self.num_processes]

        if self.config_path is None:
            self.config_path = []
        else:
            self.config_path = ['-c', self.config_path]

        if self.no_config:
            self.no_config = ['-C']
        else:
            self.no_config = []

        if self.no_config:
            self.no_config = ['-C']
        else:
            self.no_config = []

        if self.keep_going:
            self.keep_going = ['--keep_going']
        else:
            self.keep_going = []

        if self.warnings_are_errors:
            self.warnings_are_errors = ['-W']
        else:
            self.warnings_are_errors = []

        if self.error_log is None:
            self.error_log = []
        else:
            self.error_log = ['-w', self.error_log]

        if self.only_errors:
            self.only_errors = ['-Q']
        else:
            self.only_errors = []

        if self.quiet:
            self.quiet = ['-q']
        else:
            self.quiet = []

        if self.no_color:
            self.no_color = ['-N']
        else:
            self.no_color = []

        if self.nit_picky:
            self.nit_picky = ['-n']
        else:
            self.nit_picky = []

        if self.distribution.verbose:
            self.verbose = ['-' + ('v' * self.distribution.verbose)]
        else:
            self.verbose = []

        if self.sphinx_conf is not None:
            if self.no_config:
                raise RuntimeError(
                    'Cannot have an options object and also '
                    'have no config specified'
                )

            if self.config_path:
                config_path = self.config_path[:-1]
            else:
                config_path = self.source_path

            if not config_path.endswith('conf.py'):
                config_path = os.path.join(config_path, 'conf.py')

            if os.path.exists(config_path + '.backup'):
                if os.path.exists(config_path):
                    os.remove(config_path)

                os.rename(config_path + '.backup', config_path)

            if os.path.exists(config_path):
                os.rename(config_path, config_path + '.backup')
                self.config_backup = config_path + '.backup'

            if self.sphinx_conf.project is None:
                self.sphinx_conf.project = self.distribution.get_name()

            if self.sphinx_conf.version is None:
                self.sphinx_conf.version = self.distribution.get_version()

            if self.sphinx_conf.author is None:
                self.sphinx_conf.author = self.distribution.get_author()

            if self.sphinx_conf.copyright is None:
                from time import strftime

                self.sphinx_conf.copyright = strftime(
                    '%Y ' + self.sphinx_conf.project
                )

            print(self.sphinx_conf)

            with open(config_path, 'w') as f:
                f.write(str(self.sphinx_conf))

    def run(self):

        try:
            cmd_obj = self.distribution.get_command_obj('build')
            cmd_obj.ensure_finalized()
            build_lib = cmd_obj.build_lib

            if os.path.exists(build_lib):
                shutil.rmtree(build_lib)

            cmd_obj.run()

            sys.path.insert(0, build_lib)
            if self.output_path is None:
                self.output_path = os.path.join(build_lib, 'docs')

            from sphinx.cmd.build import build_main

            options = (
                self.builder_name +
                self.html_values +
                self.config_overrides +
                self.full_traceback +
                self.all_output +
                self.no_saved_environment +
                self.tag +
                self.doctree_path +
                self.num_processes +
                self.config_path +
                self.no_config +
                self.keep_going +
                self.warnings_are_errors +
                self.error_log +
                self.only_errors +
                self.quiet +
                self.no_color +
                self.nit_picky +
                [self.source_path, self.output_path]
            )

            build_main(options)
        except:
            traceback.print_exc()

        if self.config_backup is not None:
            config_file = self.config_backup.replace('.backup', '')

            os.remove(config_file)
            os.rename(self.config_backup, config_file)

