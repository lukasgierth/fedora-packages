%global debug_package %{nil}

Name:    systemctl-tui
Version: 0.4.0
Release: %autorelease
Summary: A fast, simple TUI for interacting with systemd services and their logs.
License: MIT
URL:     https://github.com/rgwood/%{name}
Source:  https://github.com/rgwood/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

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
