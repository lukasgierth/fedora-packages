%global debug_package %{nil}

Name:    skim
# renovate: datasource=github-releases depName=skim-rs/skim extractVersion=true
Version: 0.20.5
Release: 2%{?dist}
Summary: Fuzzy Finder in rust!
License: MIT
URL:     https://github.com/skim-rs/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%package -n skim-tmux
Summary: tmux script for skim fuzzy finder
Requires: skim
Requires: tmux

%description

%description -n skim-tmux

%prep
%autosetup -n %{name}-%{version}
mv shell/completion.bash shell/skim
mv shell/completion.fish shell/skim.fish
mv shell/completion.zsh shell/_skim

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
# skim
install -Dpm 0755 target/release/sk -t %{buildroot}%{_bindir}/
install -Dpm 0755 bin/sk-tmux -t %{buildroot}%{_bindir}/
install -Dpm 0644 man/man1/sk.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 man/man1/sk-tmux.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 shell/skim -t %{buildroot}%{bash_completions_dir}/
install -Dpm 0644 shell/skim.fish -t %{buildroot}%{fish_completions_dir}/
install -Dpm 0644 shell/_skim -t %{buildroot}%{zsh_completions_dir}/
# skim-tmux

%files
%license LICENSE
%doc README.md
%{_bindir}/sk
%{_mandir}/man1/sk.1.gz
%{bash_completions_dir}/skim
%{fish_completions_dir}/skim.fish
%{zsh_completions_dir}/_skim

%files -n skim-tmux
%{_bindir}/sk-tmux
%{_mandir}/man1/sk-tmux.1.gz

%changelog
%autochangelog
