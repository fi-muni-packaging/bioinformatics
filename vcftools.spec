Name:           vcftools
Version:        0.1.16
Release:        1%{?dist}
Summary:        A set of tools written in Perl and C++ for working with VCF files, such as those generated by the 1000 Genomes Project.

License:        GPLv3
URL:            https://github.com/vcftools/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  zlib-devel
BuildRequires:  make


%description
%{summary}


%prep
%autosetup


%build
./autogen.sh
%configure
%make_build


%install
%make_install


%files
%doc %{_mandir}/man1/vcftools.1.gz
%{_bindir}/%{name}*
%{_bindir}/fill-*
%{_bindir}/vcf-*
%{_datadir}/perl5/*


%changelog
* Wed May 17 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com>
- Initial package
