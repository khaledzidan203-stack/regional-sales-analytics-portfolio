# Desktop Release Policy

Compiled executable and installer artifacts are not part of the current public release.

A future installer may be published only after all applicable gates pass:

- data-free rebuild;
- analytical regression tests;
- source/app generation parity;
- publication and binary scans;
- Windows build verification;
- clean-machine installation test;
- WebView2 verification;
- installer-content review;
- approval of the exact release checksum.

Until every gate passes, documentation may describe the NSIS architecture and packaging source but must not claim a publicly validated installer.
