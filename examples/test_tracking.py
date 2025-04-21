from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

# Simulate work
for i in range(10000000):
    _ = i * i

tracker.stop()
