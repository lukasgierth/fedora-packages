%global debug_package %{nil}

Name:    gping
# renovate: datasource=github-releases depName=orf/gping extractVersion=true
Version: 1.20.1
Release: 1%{?dist}
Summary: Ping, but with a graph
License: MIT
URL:     https://github.com/orf/%{name}
Source:  %{url}/archive/refs/tags/gping-v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{name}-v%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc readme.md
%{_bindir}/%{name}

%changelog
%autochangelog
