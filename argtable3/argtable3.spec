Name:		argtable3
# renovate: datasource=github-releases depName=argtable/argtable3
Version:	3.3.1
Release:	%autorelease
Summary:	ANSI C command-line parsing library that parses GNU-style command-line options.
License:	BSD
URL:		https://github.com/argtable/argtable3
Source:		%{url}/archive/v%{version}/argtable3-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	pkgconfig
BuildRequires:	cmake

%description
Argtable3 is an open source ANSI C library that parses GNU-style command-line options with the getopt library. It simplifies command-line parsing by defining a declarative-style API that you can use to specify what your command-line syntax looks like. Argtable3 will automatically generate consistent error handling logic and textual descriptions of the command line syntax, which are essential but tedious to implement for a robust CLI program.

%package devel
Summary: Development package that includes the argtable3 header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header and development files for using argtable3

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
	-DARGTABLE3_REPLACE_GETOPT=OFF

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/pkgconfig/%{name}.pc

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
