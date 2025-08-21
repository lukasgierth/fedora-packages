Name:			blisp
# renovate: datasource=github-releases depName=pine64/blisp
Version:		0.0.5
Release:		%{autorelease}
Summary:		ISP tool for Bouffalo Labs RISC-V Microcontrollers and SoCs
License:		MIT
URL:			https://github.com/pine64/%{name}
Source:			%{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	libserialport-devel
BuildRequires:	argtable3-devel
Requires:		libblisp%{?_isa} = %{version}-%{release}

%description
Bouffalo Labs ISP (in-system-programming) tool & library: an open source tool to flash Bouffalo RISC-V MCUs.

%package -n libblisp
Summary:		Library for Bouffalo Labs RISC-V Microcontrollers and SoCs

%description -n libblisp
Library files for Bouffalo Labs RISC-V Microcontrollers and SoCs

%package -n libblisp-devel
Summary:		Development files for libblisp
Requires:		libblisp%{?_isa} = %{version}-%{release}

%description -n libblisp-devel
Development files for Bouffalo Labs RISC-V Microcontrollers and SoCs

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
	-DBLISP_BUILD_CLI=ON \
	-DBLISP_USE_SYSTEM_LIBRARIES=ON \
	-DCOMPILE_TESTS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files -n libblisp
%{_libdir}/libblisp.so.*
%ghost %{_libdir}/libblisp.a

%files -n libblisp-devel
%{_libdir}/libblisp.so
%{_includedir}/blisp*.h

%changelog
%autochangelog
