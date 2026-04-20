%global debug_package %{nil}

Name:    llmfit
# renovate: datasource=github-releases depName=AlexsJones/llmfit extractVersion=true
Version: 0.9.11
Release: 1%{?dist}
Summary: Hundreds of models & providers. One command to find what runs on your hardware.
License: MIT
URL:     https://github.com/AlexsJones/%{name}
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
install -Dpm 0755 target/release/llmfit -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/llmfit

%changelog
%autochangelog
