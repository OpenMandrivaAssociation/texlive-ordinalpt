%global tl_name ordinalpt
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Counters as ordinal numbers in Portuguese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ordinalpt
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a counter style (like \arabic, \alph and others)
which produces as output strings like "primeiro" ("first" in
Portuguese), "segundo" (second), and so on up to 1999th. Separate
counter commands are provided for different letter case variants, and
for masculine and feminine gender inflections.

