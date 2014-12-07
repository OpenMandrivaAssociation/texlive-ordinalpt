# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ordinalpt
# catalog-date 2007-02-25 09:43:45 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-ordinalpt
Version:	2.1
Release:	9
Summary:	Counters as ordinal numbers in Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ordinalpt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ordinalpt.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 754554
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 719167
- texlive-ordinalpt
- texlive-ordinalpt
- texlive-ordinalpt
- texlive-ordinalpt

