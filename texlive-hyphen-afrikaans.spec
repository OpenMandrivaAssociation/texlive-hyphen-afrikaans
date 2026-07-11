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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Afrikaans in T1/EC and UTF-8 encodings.
OpenOffice includes older patterns created by a different author, but
the patterns packaged with TeX are considered superior in quality.

