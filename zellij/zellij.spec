%global debug_package %{nil}

Name:       zellij
Version:    0.43.0
Release:    3%{?dist}
Summary:    A terminal workspace with batteries included.
License:    MIT
URL:        https://github.com/zellij-org/zellij
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo >= 1.39
BuildRequires: rust >= 1.39
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: perl-devel
BuildRequires: openssl-perl
BuildRequires: perl-FindBin
BuildRequires: perl-IPC-Cmd

%description
Zellij is a workspace aimed at developers, ops-oriented people and anyone who loves the terminal. At its core, it is a terminal multiplexer (similar to tmux and screen), but this is merely its infrastructure layer. Zellij includes a layout system, and a plugin system allowing one to create plugins in any language that compiles to WebAssembly.

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/zellij -t %{buildroot}%{_bindir}/

%files
%license LICENSE.md
%doc README.md
%{_bindir}/zellij

%changelog
%autochangelog
