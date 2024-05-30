Make an IPFS HTTP API Library. 
Use Kubo RPC API docs found in this website https://docs.ipfs.tech/reference/kubo/rpc/ as reference.
All apis must be an HTTP call to the endpoints found in Kubo RPC API docs.
There must be no third party IPFS library import. 
The library must have these functionalities and their respective apis:
1. Add a file to ipfs network
2. Add a folder to ipfs network
3. Pin a cid to local ipfs network
4. Pin a cid recursively to local ipfs
5. Remove a pinned cid
6. Get a file by cid from ipfs network
7. Get a folder by cid from ipfs network
8. Download a file by cid from ipfs network
9. Download a folder by cid from ipfs network
10. Read a file by cid from ipfs network
11. Other very important apis needed for accessing files, listing files, getting files, reading files from and into the ipfs network
All apis should have their own unit tests. The library should work and be ready to be used. The unit tests should run and should pass.
