comparison_count = 0 # Global counter
def min_max_dc(arr, low, high):
global comparison_count
# Base case: single element
if low == high:
return arr[low], arr[low]
# Base case: two elements
if high == low + 1:
comparison_count += 1
if arr[low] &lt; arr[high]:
return arr[low], arr[high]
return arr[high], arr[low]
# Divide
mid = (low + high) // 2
lmin, lmax = min_max_dc(arr, low, mid)
rmin, rmax = min_max_dc(arr, mid + 1, high)
# Conquer: combine with 2 comparisons
comparison_count += 1
overall_min = lmin if lmin &lt; rmin else rmin
comparison_count += 1
overall_max = lmax if lmax &gt; rmax else rmax
return overall_min, overall_max
def min_max_naive(arr):
mn, mx = arr[0], arr[0]
comps = 0
for x in arr[1:]:
comps += 1
if x &lt; mn: mn = x
comps += 1
if x &gt; mx: mx = x
return mn, mx, comps
# --- Demonstration on small array ---
arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]
comparison_count = 0
mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comps = comparison_count
_, _, naive_comps = min_max_naive(arr)
print(f&#39;Array: {arr}&#39;)
print(f&#39;Min: {mn}, Max: {mx}&#39;)
print(f&#39;D&amp;C Comparisons: {dc_comps}&#39;)
print(f&#39;Naive Comparisons: {naive_comps}&#39;)
# --- Performance Analysis ---
print(f&#39;\n{&quot;Size&quot;:&gt;8} {&quot;DC Comps&quot;:&gt;12} {&quot;Naive Comps&quot;:&gt;14} {&quot;Formula 3n/2-2&quot;:&gt;16}&#39;)
print(&#39;-&#39; * 56)
for size in [10, 100, 1000, 10000]:
arr = [random.randint(1, 10000) for _ in range(size)]
comparison_count = 0
mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc = comparison_count
_, _, naive = min_max_naive(arr)
formula = 3 * size // 2 - 2
print(f&#39;{size:&gt;8} {dc:&gt;12} {naive:&gt;14} {formula:&gt;16}&#39;)
