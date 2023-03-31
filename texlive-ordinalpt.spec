Name:		texlive-ordinalpt
Version:	15878
Release:	2
Summary:	Counters as ordinal numbers in Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ordinalpt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a counter style (like \arabic, \alph and
others) which produces as output strings like "primeiro"
("first" in Portuguese), "segundo" (second), and so on up to
1999th. Separate counter commands are provided for different
letter case variants, and for masculine and feminine gender
inflections.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ordinalpt/ordinalpt.sty
%doc %{_texmfdistdir}/doc/latex/ordinalpt/README
%doc %{_texmfdistdir}/doc/latex/ordinalpt/ordinalpt.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ordinalpt/ordinalpt.dtx
%doc %{_texmfdistdir}/source/latex/ordinalpt/ordinalpt.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
