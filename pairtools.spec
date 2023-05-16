Name:           pairtools
Version:        1.0.2
Release:        1%{?dist}
Summary:        CLI tools to process mapped Hi-C data

License:        MIT
URL:            https://github.com/open2c/%{name}
Source:         %{pypi_source %{name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-numpy
BuildRequires:  python3-click
BuildRequires:  python3-scipy
BuildRequires:  python3-pandas
BuildRequires:  python3-pysam
BuildRequires:  python3-pyyaml
BuildRequires:  python3-bioframe


%description
%{summary}


%prep
%autosetup


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}


%check
%pyproject_check_import
%pytest


%files -n %{name} -f %{pyproject_files}


%changelog
* Wed May 17 2023 Jiri Kyjovsky <j1.kyjovsky@gmail.com> - 1.0.2-1
- Initial package
