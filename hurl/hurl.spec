%global debug_package %{nil}

Name:    hurl
# renovate: datasource=github-releases depName=Orange-OpenSource/hurl
Version: 7.0.0
Release: %autorelease
Summary: Hurl is a command line tool that runs HTTP requests defined in a simple plain text format
License: APACHEv2
URL:     https://github.com/Orange-OpenSource/%{name}
Source:  %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: clang-devel
BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: rust

Requires: curl

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/hurl -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/hurl

%changelog
%autochangelog
