# -*- coding: utf-8 -*-


def create_property(func):
    func_name = func.__name__

    try:
        res = func(None)
    except:
        res = None

    doc = 'Default = ' + str(res)

    def fget(self):
        if func_name in self._config_options:
            return self._config_options[func_name]

        return func(self)

    def fset(self, value):
        self._config_options[func_name] = value

    def fdel(self):
        if func_name in self._config_options:
            del self._config_options[func_name]

    return property(fget=fget, fset=fset, fdel=fdel, doc=doc)


class ConfigOptions(object):

    def __init__(self):
        self._config_options = {}
        self._additional_lines = []

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if item in ConfigOptions.__dict__:
            prop = ConfigOptions.__dict__[item]
            return prop.fget(self)

        if item in self._config_options:
            return self._config_options[item]

        raise AttributeError(item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            object.__setattr__(self, key, value)
            return

        if key in ConfigOptions.__dict__:
            prop = ConfigOptions.__dict__[key]
            prop.fset(self, value)
            return

        self._config_options[key] = value

    def __delattr__(self, item):
        if item in ConfigOptions.__dict__:
            prop = ConfigOptions.__dict__[item]
            prop.fdel(self)

        elif item in self._config_options:
            del self._config_options[item]

    @create_property
    def project(self):
        pass

    @create_property
    def author(self):
        pass

    @create_property
    def copyright(self):
        pass

    @create_property
    def version(self):
        pass

    @create_property
    def release(self):
        pass

    @create_property
    def extensions(self):
        pass

    @create_property
    def source_suffix(self):
        return {'.rst': 'restructuredtext'}

    @create_property
    def source_encoding(self):
        return 'utf-8-sig'

    @create_property
    def source_parsers(self):
        pass

    @create_property
    def master_doc(self):
        return 'index'

    @create_property
    def exclude_patterns(self):
        pass

    @create_property
    def templates_path(self):
        pass

    @create_property
    def template_bridge(self):
        pass

    @create_property
    def rst_epilog(self):
        pass

    @create_property
    def rst_prolog(self):
        pass

    @create_property
    def primary_domain(self):
        return 'py'

    @create_property
    def default_role(self):
        pass

    @create_property
    def keep_warnings(self):
        return False

    @create_property
    def suppress_warnings(self):
        pass

    @create_property
    def needs_sphinx(self):
        pass

    @create_property
    def needs_extensions(self):
        pass

    @create_property
    def manpages_url(self):
        pass

    @create_property
    def nitpicky(self):
        return False

    @create_property
    def nitpick_ignore(self):
        return ()

    @create_property
    def numfig(self):
        return False

    @create_property
    def numfig_format(self):
        return {
            'figure':     'Fig. %s',
            'table':      'Table %s',
            'code-block': 'Listing %s',
            'section':    'Section'
        }

    @create_property
    def numfig_secnum_depth(self):
        return 1

    @create_property
    def smartquotes(self):
        return True

    @create_property
    def smartquotes_action(self):
        return 'qDe'

    @create_property
    def smartquotes_excludes(self):
        return {'languages': ['ja'], 'builders': ['man', 'text']}

    @create_property
    def tls_verify(self):
        return True

    @create_property
    def tls_cacerts(self):
        pass

    @create_property
    def today(self):
        pass

    @create_property
    def today_fmt(self):
        pass

    @create_property
    def highlight_language(self):
        return 'default'

    @create_property
    def highlight_options(self):
        pass

    @create_property
    def pygments_style(self):
        pass

    @create_property
    def add_function_parentheses(self):
        return True

    @create_property
    def add_module_names(self):
        return True

    @create_property
    def show_authors(self):
        return False

    @create_property
    def modindex_common_prefix(self):
        return []

    @create_property
    def trim_footnote_reference_space(self):
        pass

    @create_property
    def trim_doctest_flags(self):
        return True

    @create_property
    def language(self):
        pass

    @create_property
    def locale_dirs(self):
        return ['locales']

    @create_property
    def gettext_compact(self):
        return False

    @create_property
    def gettext_uuid(self):
        return False

    @create_property
    def gettext_location(self):
        return True

    @create_property
    def gettext_auto_build(self):
        return True

    @create_property
    def gettext_additional_targets(self):
        return []

    @create_property
    def figure_language_filename(self):
        return '{root}.{language}{ext}'

    @create_property
    def math_number_all(self):
        return False

    @create_property
    def math_eqref_format(self):
        pass

    @create_property
    def math_numfig(self):
        return True

    @create_property
    def html_theme(self):
        return 'alabaster'

    @create_property
    def html_theme_options(self):
        pass

    @create_property
    def html_theme_path(self):
        pass

    @create_property
    def html_style(self):
        pass

    @create_property
    def html_title(self):
        return str(self.project) + ' v' + str(self.version) + 'documentation'

    @create_property
    def html_short_title(self):
        return self.html_title

    @create_property
    def html_baseurl(self):
        pass

    @create_property
    def html_context(self):
        pass

    @create_property
    def html_logo(self):
        pass

    @create_property
    def html_favicon(self):
        pass

    @create_property
    def html_css_files(self):
        return []

    @create_property
    def html_js_files(self):
        return []

    @create_property
    def html_static_path(self):
        pass

    @create_property
    def html_extra_path(self):
        pass

    @create_property
    def html_last_updated_fmt(self):
        pass

    @create_property
    def html_use_smartypants(self):
        return True

    @create_property
    def html_add_permalinks(self):
        return True

    @create_property
    def html_sidebars(self):
        pass

    @create_property
    def html_additional_pages(self):
        pass

    @create_property
    def html_domain_indices(self):
        return True

    @create_property
    def html_use_index(self):
        return True

    @create_property
    def html_split_index(self):
        return False

    @create_property
    def html_copy_source(self):
        return True

    @create_property
    def html_show_sourcelink(self):
        return True

    @create_property
    def html_sourcelink_suffix(self):
        return '.txt'

    @create_property
    def html_use_opensearch(self):
        return ''

    @create_property
    def html_file_suffix(self):
        return ".html"

    @create_property
    def html_link_suffix(self):
        return self.html_file_suffix

    @create_property
    def html_show_copyright(self):
        return True

    @create_property
    def html_show_sphinx(self):
        return True

    @create_property
    def html_output_encoding(self):
        return 'utf-8'

    @create_property
    def html_compact_lists(self):
        return True

    @create_property
    def html_secnumber_suffix(self):
        return ". "

    @create_property
    def html_search_language(self):
        lang = self.language
        if lang is None:
            lang = "en"
        return lang

    @create_property
    def html_search_options(self):
        pass

    @create_property
    def html_search_scorer(self):
        return ''

    @create_property
    def html_scaled_image_link(self):
        return True

    @create_property
    def html_math_renderer(self):
        return 'mathjax'

    @create_property
    def html_experimental_html5_writer(self):
        return False

    @create_property
    def html4_writer(self):
        return False

    @create_property
    def singlehtml_sidebars(self):
        return self.html_sidebars

    @create_property
    def htmlhelp_basename(self):
        return 'pydoc'

    @create_property
    def htmlhelp_file_suffix(self):
        return ".html"

    @create_property
    def htmlhelp_link_suffix(self):
        return ".html"

    @create_property
    def applehelp_bundle_name(self):
        return self.project

    @create_property
    def applehelp_bundle_id(self):
        pass

    @create_property
    def applehelp_dev_region(self):
        return 'en-us'

    @create_property
    def applehelp_bundle_version(self):
        return '1'

    @create_property
    def applehelp_icon(self):
        pass

    @create_property
    def applehelp_kb_product(self):
        return str(self.project) + '-' + str(self.release)

    @create_property
    def applehelp_kb_url(self):
        pass

    @create_property
    def applehelp_remote_url(self):
        pass

    @create_property
    def applehelp_index_anchors(self):
        pass

    @create_property
    def applehelp_min_term_length(self):
        pass

    @create_property
    def applehelp_stopwords(self):
        lang = self.language
        if lang is None:
            lang = "en"
        return lang

    @create_property
    def applehelp_locale(self):
        lang = self.language
        if lang is None:
            lang = "en"
        return lang

    @create_property
    def applehelp_title(self):
        return str(self.project) + ' Help'

    @create_property
    def applehelp_codesign_identity(self):
        pass

    @create_property
    def applehelp_codesign_flags(self):
        pass

    @create_property
    def applehelp_indexer_path(self):
        return '/usr/bin/hiutil'

    @create_property
    def applehelp_codesign_path(self):
        return '/usr/bin/codesign'

    @create_property
    def applehelp_disable_external_tools(self):
        return False

    @create_property
    def epub_basename(self):
        return self.project

    @create_property
    def epub_theme(self):
        return 'epub'

    @create_property
    def epub_theme_options(self):
        pass

    @create_property
    def epub_title(self):
        return self.project

    @create_property
    def epub_description(self):
        return 'unknown'

    @create_property
    def epub_author(self):
        return self.author

    @create_property
    def epub_contributor(self):
        return 'unknown'

    @create_property
    def epub_language(self):
        lang = self.language

        if lang is None:
            lang = "en"
        return lang

    @create_property
    def epub_publisher(self):
        return self.author

    @create_property
    def epub_copyright(self):
        return self.copyright

    @create_property
    def epub_identifier(self):
        return 'unknown'

    @create_property
    def epub_scheme(self):
        return 'unknown'

    @create_property
    def epub_uid(self):
        return 'unknown'

    @create_property
    def epub_cover(self):
        return ()

    @create_property
    def epub_css_files(self):
        pass

    @create_property
    def epub_guide(self):
        return ()

    @create_property
    def epub_pre_files(self):
        return []

    @create_property
    def epub_post_files(self):
        return []

    @create_property
    def epub_exclude_files(self):
        return []

    @create_property
    def epub_tocdepth(self):
        return 3

    @create_property
    def epub_tocdup(self):
        return True

    @create_property
    def epub_tocscope(self):
        return 'default'

    @create_property
    def epub_fix_images(self):
        return False

    @create_property
    def epub_max_image_width(self):
        return 0

    @create_property
    def epub_show_urls(self):
        return 'inline'

    @create_property
    def epub_use_index(self):
        return self.html_use_index

    @create_property
    def epub_writing_mode(self):
        return 'horizontal'

    @create_property
    def latex_engine(self):
        return 'pdflatex'

    @create_property
    def latex_documents(self):
        pass

    @create_property
    def latex_logo(self):
        pass

    @create_property
    def latex_toplevel_sectioning(self):
        pass

    @create_property
    def latex_appendices(self):
        pass

    @create_property
    def latex_domain_indices(self):
        return True

    @create_property
    def latex_show_pagerefs(self):
        return False

    @create_property
    def latex_show_urls(self):
        return 'no'

    @create_property
    def latex_use_latex_multicolumn(self):
        return False

    @create_property
    def latex_use_xindy(self):
        pass

    @create_property
    def latex_elements(self):
        pass

    @create_property
    def latex_docclass(self):
        return {'howto': 'article', 'manual': 'report'}

    @create_property
    def latex_additional_files(self):
        pass

    @create_property
    def text_newlines(self):
        return 'unix'

    @create_property
    def text_sectionchars(self):
        return '*=-~"+`'

    @create_property
    def text_add_secnumbers(self):
        return True

    @create_property
    def text_secnumber_suffix(self):
        return ". "

    @create_property
    def man_pages(self):
        pass

    @create_property
    def man_show_urls(self):
        return False

    @create_property
    def texinfo_documents(self):
        pass

    @create_property
    def texinfo_appendices(self):
        pass

    @create_property
    def texinfo_domain_indices(self):
        return True

    @create_property
    def texinfo_show_urls(self):
        return 'footnote'

    @create_property
    def texinfo_no_detailmenu(self):
        return False

    @create_property
    def texinfo_elements(self):
        pass

    @create_property
    def qthelp_basename(self):
        return self.project

    @create_property
    def qthelp_namespace(self):
        return 'org.sphinx.' + str(self.project) + '.' + str(self.version)

    @create_property
    def qthelp_theme(self):
        return 'nonav'

    @create_property
    def qthelp_theme_options(self):
        pass

    @create_property
    def linkcheck_ignore(self):
        pass

    @create_property
    def linkcheck_retries(self):
        return 1

    @create_property
    def linkcheck_timeout(self):
        pass

    @create_property
    def linkcheck_workers(self):
        return 5

    @create_property
    def linkcheck_anchors(self):
        return True

    @create_property
    def linkcheck_anchors_ignore(self):
        return ["^!"]

    @create_property
    def xml_pretty(self):
        return True

    @create_property
    def Footnotes(self):
        pass

    @create_property
    def cpp_index_common_prefix(self):
        pass

    @create_property
    def cpp_id_attributes(self):
        pass

    @create_property
    def cpp_paren_attributes(self):
        pass

    def add_aditional_lines(self, lines):
        self._additional_lines += [lines]

    def __str__(self):
        output = ''
        for key, value in self._config_options.items():
            output += key + ' = ' + repr(value) + '\n'

        output += '\n\n'

        output += '\n\n'.join(self._additional_lines)
        return '# -*- coding: utf-8 -*-\n\n' + output + '\n'
