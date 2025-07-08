%global debug_package %{nil}

Name:    hex
Version: 0.6.0
Release: %autorelease
Summary: Futuristic take on hexdump.
License: MIT
URL:     https://github.com/sitkevij/%{name}
Source:  https://github.com/sitkevij/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description
TODO

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/hx -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/hx

%changelog
%autochangelog
