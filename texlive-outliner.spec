# revision 21095
# category Package
# catalog-ctan /macros/latex/contrib/outliner
# catalog-date 2007-01-12 15:52:44 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-outliner
Version:	20070112
Release:	1
Summary:	Change section levels easily
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/outliner
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outliner.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outliner.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Allows you to write "\Level 2 {Some heading}" instead of the
usual \section stuff; the definitions of the levels can then
easily be changed. There is a mechanism for shifting all
levels. This makes it easy to bundle existing articles into a
compilation.

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
%{_texmfdistdir}/tex/latex/outliner/outliner.sty
%doc %{_texmfdistdir}/doc/latex/outliner/outline_test.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
