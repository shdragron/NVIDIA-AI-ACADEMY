#include <stdio.h>

__global__
void initWith(float num, float *a, int N)
{

  int index = threadIdx.x + blockIdx.x * blockDim.x;
  int stride = blockDim.x * gridDim.x;

  for(int i = index; i < N; i += stride)
  {
    a[i] = num;
  }
}

__global__
void addVectorsInto(float *result, float *a, float *b, int N)
{
  int index = threadIdx.x + blockIdx.x * blockDim.x;
  int stride = blockDim.x * gridDim.x;

  for(int i = index; i < N; i += stride)
  {
    result[i] = a[i] + b[i];
  }
}

void checkElementsAre(float target, float *vector, int N)
{
  for(int i = 0; i < N; i++)
  {
    if(vector[i] != target)
    {
      printf("FAIL: vector[%d] - %0.0f does not equal %0.0f\n", i, vector[i], target);
      exit(1);
    }
  }
  printf("Success! All values calculated correctly.\n");
}

int main()
{
  int deviceId;
  int numberOfSMs;

  cudaGetDevice(&deviceId);
  cudaDeviceGetAttribute(&numberOfSMs, cudaDevAttrMultiProcessorCount, deviceId);

  const int N = 2<<24;
  size_t size = N * sizeof(float);

  float *host_a, *device_a ;
  float *host_b, *device_b ;
  float *host_c, *device_c ;
  
  

  cudaMallocHost(&host_a, size);
  cudaMallocHost(&host_b, size);
  cudaMallocHost(&host_c, size);
  
    
  cudaMalloc(&device_a, size);
  cudaMalloc(&device_b, size);
  cudaMalloc(&device_c, size);

    

  size_t threadsPerBlock;
  size_t numberOfBlocks;

  threadsPerBlock = 256;
  numberOfBlocks = 32 * numberOfSMs;

  cudaError_t addVectorsErr;
  cudaError_t asyncErr;

  /*
   * Create 3 streams to run initialize the 3 data vectors in parallel.
   */

  cudaStream_t stream1, stream2, stream3;
  cudaStreamCreate(&stream1);
  cudaStreamCreate(&stream2);
  cudaStreamCreate(&stream3);

  /*
   * Give each `initWith` launch its own non-standard stream.
   */
  cudaMemcpy(device_a, host_a, size, cudaMemcpyHostToDevice);
  cudaMemcpy(device_b, host_b, size, cudaMemcpyHostToDevice);
  cudaMemcpy(device_c, host_c, size, cudaMemcpyHostToDevice);
    
    
  initWith<<<numberOfBlocks, threadsPerBlock, 0, stream1>>>(3, device_a, N);
  initWith<<<numberOfBlocks, threadsPerBlock, 0, stream2>>>(4, device_b, N);
  initWith<<<numberOfBlocks, threadsPerBlock, 0, stream3>>>(0, device_c, N);

  addVectorsInto<<<numberOfBlocks, threadsPerBlock>>>(device_c, device_a, device_b, N);

  cudaMemcpy(host_a, device_a, size, cudaMemcpyDeviceToHost);
  cudaMemcpy(host_b, device_b, size, cudaMemcpyDeviceToHost);
  cudaMemcpy(host_c, device_c, size, cudaMemcpyDeviceToHost);
  
    
  addVectorsErr = cudaGetLastError();
  if(addVectorsErr != cudaSuccess) printf("Error: %s\n", cudaGetErrorString(addVectorsErr));

  asyncErr = cudaDeviceSynchronize();
  if(asyncErr != cudaSuccess) printf("Error: %s\n", cudaGetErrorString(asyncErr));


  checkElementsAre(7, host_c, N);

  /*
   * Destroy streams when they are no longer needed.
   */

  cudaStreamDestroy(stream1);
  cudaStreamDestroy(stream2);
  cudaStreamDestroy(stream3);

  cudaFree(device_a);
  cudaFree(device_b);
  cudaFree(device_c);
  cudaFreeHost(host_a);
  cudaFreeHost(host_b);
  cudaFreeHost(host_c);
}

!nvcc -o vector-add-manual-alloc 06-stream-init/solutions/01-stream-init-solution.cu -run