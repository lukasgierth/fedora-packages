%global debug_package %{nil}

Name:    mise-completions-sync
# renovate: datasource=github-releases depName=alltuner/mise-completions-sync extractVersion=true
Version: 0.5.7
Release: 2%{?dist}
Summary: Automatically sync shell completions for tools managed by mise
License: MIT
URL:     https://github.com/alltuner/%{name}
Source0:  %{url}/archive/refs/tags/v%{version}.tar.gz
Source1: mise-completions-sync.sh
Source2: 21-mise-completions-sync.fish

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
install -d %{buildroot}/usr/share/fish/vendor_conf.d
install -d %{buildroot}/etc/profile.d
install -Dpm 0644 %{_sourcedir}/mise-completions-sync.sh -t %{buildroot}/etc/profile.d/
install -Dpm 0644 %{_sourcedir}/21-mise-completions-sync.fish -t %{buildroot}/usr/share/fish/vendor_conf.d/

%files
%license LICENSE
%doc README.md
%{_bindir}/misecompsync
/etc/profile.d/mise-completions-sync.sh
/usr/share/fish/vendor_conf.d/21-mise-completions-sync.fish

%changelog
%autochangelog
