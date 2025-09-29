%global debug_package %{nil}

Name:    rmt-rs
# renovate: datasource=github-releases depName=AmineZouitine/rmt.rs extractVersion=true
Version: 0.2.1
Release: 1%{?dist}
Summary: Rmt is similar to the rm command but saves the deleted elements in the trash and restores them. Rmt is written in Rust
License: MIT
URL:     https://github.com/AmineZouitine/rmt.rs
Source:  %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n rmt.rs-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/rmt -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/rmt

%changelog
%autochangelog
