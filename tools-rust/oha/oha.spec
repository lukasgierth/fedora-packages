%global debug_package %{nil}

Name:    oha
# renovate: datasource=github-releases depName=hatoo/oha extractVersion=true
Version: 1.12.0
Release: 1%{?dist}
Summary: Ohayou(おはよう), HTTP load generator, inspired by rakyll/hey with tui animation.
License: MIT
URL:     https://github.com/hatoo/%{name}
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
install -Dpm 0755 target/release/oha -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/oha

%changelog
%autochangelog
