%global debug_package %{nil}

Name:    starship
# renovate: datasource=github-releases depName=starship/starship extractVersion=true
Version: 1.25.1
Release: 1%{?dist}
Summary: The minimal, blazing-fast, and infinitely customizable prompt for any shell!
License: ISC
URL:     https://github.com/%{name}/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
