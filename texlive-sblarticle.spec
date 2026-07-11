%global tl_name sblarticle
%global tl_revision 78599

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A LaTeX class for SBL style articles and papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sblarticle
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sblarticle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sblarticle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sblarticle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX class for producing articles and papers
conforming to the style required by the Society of Biblical Literature.
It depends on sblfonts for language support and biblatex-sbl for
referencing.

