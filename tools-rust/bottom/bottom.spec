%global debug_package %{nil}

Name:    bottom
# renovate: datasource=github-releases depName=ClementTsang/bottom extractVersion=true
Version: 0.12.3
Release: 1%{?dist}
Summary: Yet another cross-platform graphical process/system monitor.
License: MIT
URL:     https://github.com/ClementTsang/%{name}
Source:  %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust > 1.85

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
export BTM_GENERATE=true
cargo build --release --locked

%install
install -Dpm 0644 target/tmp/bottom/completion/_btm -t %{buildroot}%{zsh_completions_dir}/_btm
install -Dpm 0644 target/tmp/bottom/completion/btm.bash -t %{buildroot}%{bash_completions_dir}/btm.bash
install -Dpm 0644 target/tmp/bottom/completion/btm.fish -t %{buildroot}%{fish_completions_dir}/btm.fish
install -Dpm 0644 target/tmp/bottom/manpage/btm.1 -t %{buildroot}%{_mandir}/man1/btm.1
install -Dpm 0755 target/release/btm -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/btm
%{_mandir}/man1/btm.1
%{bash_completions_dir}/btm.bash
%{fish_completions_dir}/btm.fish
%{zsh_completions_dir}/_btm

%changelog
%autochangelog
