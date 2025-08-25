%global debug_package %{nil}

Name:    skim
# renovate: datasource=github-releases depName=skim-rs/skim
Version: 0.20.5
Release: %autorelease
Summary: Fuzzy Finder in rust!
License: MIT
URL:     https://github.com/skim-rs/%{name}
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
install -Dpm 0755 target/release/sk -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/sk

%changelog
%autochangelog
