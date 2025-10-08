%global debug_package %{nil}

Name:    deno
# renovate: datasource=github-releases depName=denoland/deno extractVersion=true
Version: 2.5.3
Release: 1%{?dist}
Summary: A modern runtime for JavaScript and TypeScript.
License: MIT
URL:     https://github.com/denoland/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: clang
BuildRequires: cmake
BuildRequires: rust >= 1.89.0
BuildRequires: glib2-devel

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
