# revision 25990
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-afrikaans
Version:	20120611
Release:	9
Summary:	Afrikaans hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-afrikaans.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Afrikaans in T1/EC and UTF-8
encodings. OpenOffice includes older patterns created by a
different author, but the patterns packaged with TeX are
considered superior in quality.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-afrikaans
%_texmf_language_def_d/hyphen-afrikaans
%_texmf_language_lua_d/hyphen-afrikaans

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-afrikaans <<EOF
\%% from hyphen-afrikaans:
afrikaans loadhyph-af.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-afrikaans
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-afrikaans <<EOF
\%% from hyphen-afrikaans:
\addlanguage{afrikaans}{loadhyph-af.tex}{}{1}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-afrikaans
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-afrikaans <<EOF
-- from hyphen-afrikaans:
	['afrikaans'] = {
		loader = 'loadhyph-af.tex',
		lefthyphenmin = 1,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-af.pat.txt',
		hyphenation = 'hyph-af.hyp.txt',
	},
EOF


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120611-1
+ Revision: 804683
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120124-1
+ Revision: 767505
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 759891
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718633
- texlive-hyphen-afrikaans
- texlive-hyphen-afrikaans
- texlive-hyphen-afrikaans
- texlive-hyphen-afrikaans

