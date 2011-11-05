# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ordinalpt
# catalog-date 2007-02-25 09:43:45 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-ordinalpt
Version:	2.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a counter style (like \arabic, \alph and
others) which produces as output strings like "primeiro"
("first" in Portuguese), "segundo" (second), and so on up to
1999th. Separate counter commands are provided for different
letter case variants, and for masculine and feminine gender
inflections.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ordinalpt/ordinalpt.sty
%doc %{_texmfdistdir}/doc/latex/ordinalpt/README
%doc %{_texmfdistdir}/doc/latex/ordinalpt/ordinalpt.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ordinalpt/ordinalpt.dtx
%doc %{_texmfdistdir}/source/latex/ordinalpt/ordinalpt.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
