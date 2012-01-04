# revision 21095
# category Package
# catalog-ctan /macros/latex/contrib/outliner
# catalog-date 2007-01-12 15:52:44 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-outliner
Version:	20070112
Release:	2
Summary:	Change section levels easily
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/outliner
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outliner.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outliner.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Allows you to write "\Level 2 {Some heading}" instead of the
usual \section stuff; the definitions of the levels can then
easily be changed. There is a mechanism for shifting all
levels. This makes it easy to bundle existing articles into a
compilation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/outliner/outliner.sty
%doc %{_texmfdistdir}/doc/latex/outliner/outline_test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
