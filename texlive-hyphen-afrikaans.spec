%global tl_name hyphen-afrikaans
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Afrikaans hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-afrikaans
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-afrikaans.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Afrikaans in T1/EC and UTF-8 encodings.
OpenOffice includes older patterns created by a different author, but
the patterns packaged with TeX are considered superior in quality.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-afrikaans:
afrikaans loadhyph-af.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-afrikaans:
\addlanguage{afrikaans}{loadhyph-af.tex}{}{1}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-afrikaans:
['afrikaans'] = {
	loader = 'loadhyph-af.tex',
	lefthyphenmin = 1,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-af.pat.txt',
	hyphenation = 'hyph-af.hyp.txt',
},
TL_HYPHEN_EOF
