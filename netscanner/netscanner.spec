%global debug_package %{nil}

Name:    netscanner
Version: 0.6.3
Release: %autorelease
Summary: Network scanner & diagnostic tool.
License: MIT
URL:     https://github.com/Chleba/%{name}
Source:  https://github.com/Chleba/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/netscanner -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/netscanner

%changelog
%autochangelog
