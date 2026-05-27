%global debug_package %{nil}

Name:    mise-completions-sync
# renovate: datasource=github-releases depName=alltuner/mise-completions-sync extractVersion=true
Version: 0.5.7
Release: 1%{?dist}
Summary: Automatically sync shell completions for tools managed by mise
License: MIT
URL:     https://github.com/alltuner/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

Requires: mise

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/misecompsync -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/misecompsync

%changelog
%autochangelog
