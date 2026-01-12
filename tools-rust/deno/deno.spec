%global debug_package %{nil}

Name:    deno
# renovate: datasource=github-releases depName=denoland/deno extractVersion=true
Version: 2.6.4
Release: 1%{?dist}
Summary: A modern runtime for JavaScript and TypeScript.
License: MIT
URL:     https://github.com/denoland/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: clang
BuildRequires: clang-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: llvm17-devel
BuildRequires: protobuf-compiler
BuildRequires: rust >= 1.90.0

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

# completions
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
target/release/%{name} completions bash > %{buildroot}%{bash_completions_dir}/%{name}.sh
target/release/%{name} completions fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
target/release/%{name} completions zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{bash_completions_dir}/%{name}.sh
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
