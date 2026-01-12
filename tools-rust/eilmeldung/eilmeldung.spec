%global debug_package %{nil}

Name:    eilmeldung
# renovate: datasource=github-releases depName=christo-auer/eilmeldung extractVersion=true
Version: 0.7.4
Release: 1%{?dist}
Summary: eilmeldung is a TUI RSS reader based on the awesome news-flash library
License: GPLv3
URL:     https://github.com/christo-auer/%{name}
Source:  %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: clang
BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: perl
BuildRequires: rust
BuildRequires: sqlite-devel

%description

%prep
%autosetup -n %{name}-%{version}

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
