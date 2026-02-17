%global debug_package %{nil}

Name:    hurl
# renovate: datasource=github-releases depName=Orange-OpenSource/hurl extractVersion=true
Version: 7.1.0
Release: 1%{?dist}
Summary: Hurl is a command line tool that runs HTTP requests defined in a simple plain text format
License: Apache-2.0
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
Recommends: hurlfmt

%package -n hurlfmt
Summary:	Formatter Tool for Hurl

%description

%description -n hurlfmt

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
# hurl
install -Dpm 0755 target/release/hurl -t %{buildroot}%{_bindir}/
install -Dpm 0644 docs/manual/hurl.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 completions/hurl.bash -t %{buildroot}%{bash_completions_dir}/
install -Dpm 0644 completions/hurl.fish -t %{buildroot}%{fish_completions_dir}/
install -Dpm 0644 completions/_hurl -t %{buildroot}%{zsh_completions_dir}/
# hurlfmt
install -Dpm 0755 target/release/hurlfmt -t %{buildroot}%{_bindir}/
install -Dpm 0644 docs/manual/hurlfmt.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 completions/hurlfmt.bash -t %{buildroot}%{bash_completions_dir}/
install -Dpm 0644 completions/hurlfmt.fish -t %{buildroot}%{fish_completions_dir}/
install -Dpm 0644 completions/_hurlfmt -t %{buildroot}%{zsh_completions_dir}/

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/hurl
%{_mandir}/man1/hurl.1.gz
%{bash_completions_dir}/hurl.bash
%{fish_completions_dir}/hurl.fish
%{zsh_completions_dir}/_hurl

%files -n hurlfmt
%{_bindir}/hurlfmt
%{_mandir}/man1/hurlfmt.1.gz
%{bash_completions_dir}/hurlfmt.bash
%{fish_completions_dir}/hurlfmt.fish
%{zsh_completions_dir}/_hurlfmt

%changelog
%autochangelog
