# sphinx-distutils-extension
Allows for building sphinx documentation from distutils.core.setup

There are 2 ways this can be used. one is if you want to use a conf.py
file for sphinx that you have already made. and you can use the
command line arguments to alter anything in that config that you may
want to.

or you can create a conf.py file using this package.


Command line arguments are almost the same as what is used in sphinx
```
python setup.py build_docs --help

Options for 'build_docs' command:
  --builder-name (-b)          compiler to use. Can be one of the following -
                               html, dirhtml, singlehtml, htmlhelp, qthelp,
                               devhelp, epub, applehelp, latex, man, texinfo,
                               text, gettext, doctest, linkcheck, xml,
                               pseudoxml the following builders are only
                               available if make mode is being used -
                               latexpdf, info  default is html
  --make-mode (-M)             Uses the Sphinx make_mode module, which
                               provides the same build functionality as a
                               default Makefile or Make.bat. In addition to
                               all Sphinx Builders, the following build
                               pipelines are available: latexpdf, info
  --all-output (-a)            If given, always write all output files. The
                               default is to only write output files for new
                               and changed source files. (This may not apply
                               to all builders.
  --no-saved-environment (-E)  DonΓÇÖt use a saved environment (the structure
                               caching all cross-references), but rebuild it
                               completely. The default is to only read and
                               parse source files that are new or have changed
                               since the last run.
  --tag (-t)                   Define the tag tag. This is relevant for only
                               directives that only include their content if
                               this tag is set.
  --doctree-path (-d)          Since Sphinx has to read and parse all source
                               files before it can write an output file, the
                               parsed source files are cached as 'doctree
                               pickles'. Normally, these files are put in a
                               directory called .doctrees under the build
                               directory; with this option you can select a
                               different cache directory (the doctrees can be
                               shared between all builders).
  --num-processes (-j)         Distribute the build over N processes in
                               parallel, to make building on multiprocessor
                               machines more effective. Note that not all
                               parts and not all builders of Sphinx can be
                               parallelized. If auto argument is given, Sphinx
                               uses the number of CPU cores. default is auto
  --config-path (-c)           DonΓÇÖt look for the conf.py in the source
                               directory, but use the given configuration
                               directory instead. Note that various other
                               files and paths given by configuration values
                               are expected to be relative to the
                               configuration directory, so they will have to
                               be present at this location too.
  --no-config (-C)             DonΓÇÖt look for a configuration file; only
                               take options via the -D option.
  --nit-picky (-n)             Run in nit-picky mode. Currently, this
                               generates warnings for all missing references.
                               See the config value nitpick_ignore for a way
                               to exclude some references as 'known missing'.
  --no-color (-N)              Do not emit colored output.
  --quiet (-q)                 Do not output anything on standard output, only
                               write warnings and errors to standard error.
  --only-errors (-Q)           Do not output anything on standard output, also
                               suppress warnings. Only errors are written to
                               standard error.
  --error-log (-w)             Write warnings (and errors) to the given file,
                               in addition to standard error.
  --warnings-are-errors (-W)   Turn warnings into errors. This means that the
                               build stops at the first warning and sphinx-
                               build exits with exit status 1.
  --keep-going                 With -W option, keep going processing when
                               getting warnings to the end of build, and
                               sphinx-build exits with exit status 1.
  --full-traceback (-T)        Display the full traceback when an unhandled
                               exception occurs. Otherwise, only a summary is
                               displayed and the traceback information is
                               saved to a file for further analysis.
  --output-path                Output path. defaults to {source path}/_build
  --source-path                Path to the source files. defaults to {current
                               path}/docs
  --config-overrides (-D)      Override a configuration value set in the
                               conf.py file. The value must be a number,
                               string, list or dictionary value. We are not
                               able to directly duplicate the command line
                               syntax from Sphinx. There are some changes
                               needed to be made in order to get this
                               parameter to work properly. each entry will be
                               setting=value separated by a semicolon
                               setting=value;setting=value;setting=value For
                               lists, html_theme_path=path1,path2. For
                               dictionary values, supply the setting name and
                               key like this:
                               latex_elements.docclass=scrartcl. For boolean
                               values, use 0 or 1 as the value.
  --html-values (-A)           Make the name assigned to value in the HTML
                               templates. We are not able to directly
                               duplicate the command line syntax from Sphinx.
                               There are some changes needed to be made in
                               order to get this parameter to work properly.
                               each entry will be setting=value separated by a
                               semicolon
                               setting=value;setting=value;setting=value

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help
```


Example Usage of creating a conf.py file using this module

```python

from sphinx_distutils import build_docs, ConfigOptions
from setuptools import setup

sphinx_conf = ConfigOptions()
build_docs.sphinx_conf = sphinx_conf

# -- GENERAL options ------------------------------------------------------
sphinx_conf.suppress_warnings = ['image.nonlocal_uri']
sphinx_conf.extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.fulltoc',
    'sphinx_sitemap',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram'
]

sphinx_conf.templates_path = ['_templates']
sphinx_conf.source_suffix = '.rst'
sphinx_conf.master_doc = 'index'
sphinx_conf.version = project version
sphinx_conf.release = project revision
sphinx_conf.exclude_patterns = ['_build']
sphinx_conf.add_function_parentheses = True
sphinx_conf.show_authors = True
sphinx_conf.pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------
sphinx_conf.html_baseurl = '/docs/'
sphinx_conf.html_theme = 'groundwork'
sphinx_conf.html_theme_options = {
    "sidebar_width": '240px',
    "stickysidebar": True,
    "stickysidebarscrollable": True,
    "contribute": True,
    "github_fork": "github user/repository",
    "github_user": "github user",
}
sphinx_conf.html_theme_path = ["_themes"]
sphinx_conf.html_title = 'python-openzwave'
sphinx_conf.html_logo = '_static/images/logo.png'
sphinx_conf.html_static_path = ['_static']
sphinx_conf.html_domain_indices = True
sphinx_conf.html_use_index = True
sphinx_conf.html_split_index = True
sphinx_conf.html_show_sourcelink = False
sphinx_conf.html_show_sphinx = False
sphinx_conf.html_show_copyright = True
sphinx_conf.htmlhelp_basename = 'project name'

# -- Options for LATEX output ---------------------------------------------
sphinx_conf.latex_elements = {}
sphinx_conf.latex_documents = [
  ('index', 'project name.tex', u'project name Documentation',
   'author', 'manual'),
]

# -- Options for MAN PAGES output -----------------------------------------
sphinx_conf.man_pages = [
    ('index', 'project name', u'project name Documentation',
     [u'author'], 1)
]

# -- Options for TEXT INFO output -----------------------------------------
sphinx_conf.texinfo_documents = [
    (
        'index',
        'project name',
        'project name Documentation',
        'author',
        'project name',
        'One line description of project.',
        'Miscellaneous'
    ),
]

sphinx_conf.add_aditional_lines(
    "def setup(app):\n    app.add_stylesheet('css/project name.css')\n"
)


setup(
    name='project name',
    author='author',
    author_email='author@gmail.com',
    version='1.0.0',
    setup_requires=[
        'Sphinx==1.8.5',
        'groundwork-sphinx-theme>=1.0.9',
        'sphinx-sitemap>=1.0.2',
        'sphinxcontrib-blockdiag>=1.5.5',
        'sphinxcontrib-nwdiag>=0.9.5',
        'sphinxcontrib-actdiag>=0.8.5',
        'sphinxcontrib-seqdiag>=0.8.5',
        'sphinxcontrib-fulltoc>=1.2.0',
    ],
    zip_safe=False,
    url='project url',
    ext_modules=[],
    options=dict(
        build_docs=dict(
            builder_name='html',
            full_traceback=True,
            # output_path='docs/_build',
            source_path='docs'
        )
    ),
    libraries=[],
    install_requires=[],
    cmdclass=dict(
        build_docs=build_docs
    ),
    packages=(),
    entry_points=dict(),
    package_dir=dict(),
    description='project description',
    long_description='project long description',
    download_url='project download url',
    keywords=[],
    classifiers=[
        "Topic :: System :: Hardware",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD",
        "Programming Language :: C++",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        (
            "License :: OSI Approved :: "
            "GNU General Public License v3 or later (GPLv3+)"
        ),
    ],
)

```

this module will default to /docs being the directory for documentation
if one is not supplied. The output of the documentation build process
is going to be the path either you supply or the build path that is
used in the setup program


If you want to install this library as a setup_requirement you will need 
to create a dummy setup program to handle that but of it. Here is a code 
example of how to do this. You would place this at the very top of your 
setup.py file.


``` python

from setuptools import setup

try:
    import sphinx_distutils
except ImportError:

    from setuptools import Command

    class install_setup_requirements(Command):
        initilize_options = lambda x: None
        finalize_options = lambda x: None
        run = lambda x: None

    setup(
        name='Install Setup Requirements',
        version='1.0.0',
        setup_requires=['sphinx-distutils-extension']
        dependency_links = [
            'https://github.com/kdschlosser/sphinx-distutils-extension/tarball'
            '/master#egg=sphinx_distutils'
        ]
        script_args=['install_setup_requirements']
        cmdclass=dict(
            install_setup_requirements=install_setup_requirements
        )
    )

    import sphinx_distutils

``` 


