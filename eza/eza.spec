%global debug_package %{nil}

Name:    eza
Version: 0.23.0
Release: %autorelease
Summary: A modern replacement for ls
# Main package is EUPL-1.2, remaining licenses are from statically linked dependencies
License: EUPL-1.2 AND MPL-2.0 AND Unicode-3.0 AND (MIT OR Apache-2.0) AND (Unlicense OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (MIT OR Apache-2.0 OR CC0-1.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (0BSD OR MIT OR Apache-2.0)
URL:     https://github.com/eza-community/%{name}
Source:  https://github.com/eza-community/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: pandoc

%description
eza is a modern, maintained replacement for the venerable file-listing
command-line program ls that ships with Unix and Linux operating systems,
giving it more features and better defaults.
It uses colours to distinguish file types and metadata.
It knows about symlinks, extended attributes, and Git.
And it’s small, fast, and just one single binary.

By deliberately making some decisions differently,
eza attempts to be a more featureful, more user-friendly version of ls.

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

# Generate license documentation
cargo tree --workspace --edges no-build,no-dev,no-proc-macro --no-dedupe --prefix none --format '{l}' | sort -u > LICENSE.summary
cargo tree --workspace --edges no-build,no-dev,no-proc-macro --no-dedupe --prefix none --format '{l}: {p}' | sort -u > LICENSE.dependencies

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/
# Man
mkdir target/man
for page in eza.1 eza_colors.5 eza_colors-explanation.5; do
    sed "s/\$version/v%{version}/g" "man/${page}.md" | pandoc --standalone -f markdown -t man > "target/man/${page}"
done;
install -Dpm 0644 target/man/eza.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 target/man/eza_colors.5 -t %{buildroot}/%{_mandir}/man5/
install -Dpm 0644 target/man/eza_colors-explanation.5 -t %{buildroot}/%{_mandir}/man5/
# Shell completions
install -Dpm 0644 completions/bash/%{name} -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 completions/fish/%{name}.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 completions/zsh/_%{name} -t %{buildroot}/%{zsh_completions_dir}

%files
%license LICENSE.txt LICENSE.summary LICENSE.dependencies
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/eza.1*
%{_mandir}/man5/eza_colors*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
