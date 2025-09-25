%global debug_package %{nil}

Name:    hex-rs
# renovate: datasource=github-releases depName=sitkevij/hex extractVersion=true
Version: 0.6.0
Release: 2%{?dist}
Summary: Futuristic take on hexdump.
License: MIT
URL:     https://github.com/sitkevij/hex
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n hex-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/hx -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/hx

%changelog
%autochangelog
