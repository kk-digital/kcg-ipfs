Name: CID Manager Library

Instructions:
1. Make a Cid Manager Library.
2. There must be a CidData class. It must have these fields:
    * string named Cid
    * Sha256 Hash
3. There must be a CidManager class. It must have these fields:
    * List of CidData called CidDataList
4. The CidManager class must have these methods:
   * Add a CidData entry to CidDataList
   * Serialize the list of CidData to one json per item. 
     * The filename of each json file must be the CidData's Hash. 
     * It should keep track of the output folder count. Folder count starts at 0. 
     * It should save the json files to a folder named "Cid" + the current folder count with 4 digit padding. 
     * Once the output folder's size exceeds 500MB, it should increment the folder count, create new folder named "Cid" + the current folder count with 4 digit padding,
     and save the rest of the json file to the new folder. Repeat when folder size exceeds 500MB. 
     * All of these sub-folders should be saved in a parent output directory with default as "./output".
   * Deserialize list of CidData from a given directory with multiple json files.
5. Testing requirements:
   * There must be a unit test for all methods of the CidManager.
   * Each test must run and pass their asserts.
   * Use mock data in the tests.