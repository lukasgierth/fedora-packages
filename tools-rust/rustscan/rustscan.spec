%global debug_package %{nil}

Name:    rustscan
# renovate: datasource=github-releases depName=bee-san/RustScan extractVersion=true
Version: 2.4.1
Release: 2%{?dist}
Summary: The Modern Port Scanner. Find ports quickly (3 seconds at its fastest). Run scripts through our scripting engine (Python, Lua, Shell supported).
License: GPL-3.0-or-later
URL:     https://github.com/bee-san/rustscan
Source:  %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

Requires: nmap

%description

%prep
%autosetup -n RustScan-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
