%global debug_package %{nil}

Name:    rustnet
# renovate: datasource=github-releases depName=domcyrus/rustnet extractVersion=true
Version: 0.16.1
Release: 1%{?dist}
Summary: A cross-platform network monitoring terminal UI tool built with Rust.
License: Apache-2.0
URL:     https://github.com/domcyrus/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust >= 1.88.0
BuildRequires: libpcap-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: clang
BuildRequires: llvm

Requires: libpcap
Requires: elfutils-libelf

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --features ebpf
# cargo build --release --features ebpf --locked

%install
install -Dpm 0755 target/release/rustnet -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/rustnet

%changelog
%autochangelog
