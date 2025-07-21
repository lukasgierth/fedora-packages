%global debug_package %{nil}

Name:    hex-rs
Version: 0.6.0
Release: %autorelease
Summary: Futuristic take on hexdump.
License: MIT
URL:     https://github.com/sitkevij/hex
Source:  https://github.com/sitkevij/hex/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n hex-%{version}

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
