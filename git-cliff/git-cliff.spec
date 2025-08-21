%global debug_package %{nil}

Name:    git-cliff
# renovate: datasource=github-releases depName=orhun/git-cliff
Version: 2.10.0
Release: %autorelease
Summary: A highly customizable Changelog Generator that follows Conventional Commit specifications.
License: MIT
URL:     https://github.com/orhun/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust >= 1.75.0
BuildRequires: libgit2-devel
BuildRequires: zlib

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/git-cliff -t %{buildroot}%{_bindir}/

%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/git-cliff

%changelog
%autochangelog
