%global debug_package %{nil}

Name:    broot
# renovate: datasource=github-releases depName=Canop/broot extractVersion=true
Version: 1.54.0
Release: 1%{?dist}
Summary: A new way to see and navigate directory trees
License: MIT
URL:     https://github.com/Canop/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: libxcb

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked --features clipboard

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/
cp man/page %{name}.1
install -Dpm 0644 %{name}.1 -t %{buildroot}%{_mandir}/man1/

# shell completions
target/release/%{name} --print-shell-function bash > %{name}.bash
target/release/%{name} --print-shell-function fish > %{name}.fish
target/release/%{name} --print-shell-function zsh > _%{name}
install -Dpm 0644 %{name}.bash -t %{buildroot}%{bash_completions_dir}/
install -Dpm 0644 %{name}.fish -t %{buildroot}%{fish_completions_dir}/
install -Dpm 0644 _%{name} -t %{buildroot}%{zsh_completions_dir}/

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{bash_completions_dir}/%{name}.bash
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
