%global commit e45941c45e2418b2bb7e3dab49468a8f4d132439
%global date 20250304
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global pre %{date}.%{shortcommit}

Name:			blisp
Version:		0.0.4
Release:		%{autorelease}%{?pre:~%pre}
Summary:		ISP tool for Bouffalo Labs RISC-V Microcontrollers and SoCs
License:		MIT
URL:			https://github.com/pine64/%{name}
Source0:		https://github.com/pine64/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# Fix tests path
Patch0:			blisp-gtest.patch

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gtest-devel
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
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake \
	-DBLISP_BUILD_CLI=ON \
	-DBLISP_USE_SYSTEM_LIBRARIES=ON \
	-DCOMPILE_TESTS=ON

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

