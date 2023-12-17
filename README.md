# GoitNeo Python Project


### Overall architecture

![Architecture](/docs/architecture.png)

**This application consist of the following services:**

- [core](./core/) - the main part of the application contains all the logic and persists data in the file system.
- [cli](./apps/cli/) - command line application which handle user input and render output from **core** service
- [web](./apps/web/) - TBD