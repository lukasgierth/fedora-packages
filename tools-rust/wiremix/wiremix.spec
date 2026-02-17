%global debug_package %{nil}

Name:    wiremix
# renovate: datasource=github-releases depName=tsowell/wiremix extractVersion=true
Version: 0.9.0
Release: 1%{?dist}
Summary: Simple TUI audio mixer for PipeWire
License: MIT OR Apache-2.0
URL:     https://github.com/tsowell/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: clang
BuildRequires: pipewire-devel
BuildRequires: pkgconf
BuildRequires: rust

Requires: pipewire

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/wiremix -t %{buildroot}%{_bindir}/

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%doc README.md
%{_bindir}/wiremix

%changelog
%autochangelog
