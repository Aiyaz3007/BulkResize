# BulkResize
**Resize Bulk Images
**

parser.add_argument('-r','--resize', nargs='+', help="pass the resize resolution", type=int)

parser.add_argument("-s","--source", help="pass the source directory" )

parser.add_argument("-t","--target", help="pass the target directory" )

**Command**:

python resizeBulkImage.py -r 100 100 -s myData -t destination
                           --resize 100 100 --source myData --target destination
