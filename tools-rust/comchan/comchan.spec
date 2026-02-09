%global debug_package %{nil}

Name:    comchan
# renovate: datasource=github-releases depName=Vaishnav-Sabari-Girish/ComChan extractVersion=true
Version: 0.2.5
Release: 1%{?dist}
Summary: A Blazingly Fast Minimal Serial Monitor written in Rust
License: MIT
URL:     https://github.com/Vaishnav-Sabari-Girish/ComChan
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: rust-libudev-devel

%description

%prep
%autosetup -n ComChan-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md docs/
%{_bindir}/%{name}

%changelog
%autochangelog
