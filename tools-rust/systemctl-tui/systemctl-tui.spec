%global debug_package %{nil}

Name:    systemctl-tui
# renovate: datasource=github-releases depName=rgwood/systemctl-tui extractVersion=true
Version: 0.5.1
Release: 1%{?dist}
Summary: A fast, simple TUI for interacting with systemd services and their logs.
License: MIT
URL:     https://github.com/rgwood/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/systemctl-tui -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/systemctl-tui

%changelog
%autochangelog
