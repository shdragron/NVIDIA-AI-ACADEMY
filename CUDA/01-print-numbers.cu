#include <stdio.h>

__global__ void printNumber(int number)
{
  printf("%d\n", number);
}

int main()
{
  cudaStream_t streamA,streamB,streamC,streamD,streamE;       // CUDA streams are of type `cudaStream_t`.
  cudaStreamCreate(&streamA);
  cudaStreamCreate(&streamB);
  cudaStreamCreate(&streamC);
  cudaStreamCreate(&streamD);
  cudaStreamCreate(&streamE);
    
  
  

  printNumber<<<1, 1, 0, streamA>>>(0);
  printNumber<<<1, 1, 0, streamB>>>(1);
  printNumber<<<1, 1, 0, streamC>>>(2);
  printNumber<<<1, 1, 0, streamD>>>(3);
  printNumber<<<1, 1, 0, streamE>>>(4);
    

    
  cudaDeviceSynchronize();
  cudaStreamDestroy(streamA);
  cudaStreamDestroy(streamB);
  cudaStreamDestroy(streamC);
  cudaStreamDestroy(streamD);
  cudaStreamDestroy(streamE);
  
  
}

!nvcc -o print-numbers 05-stream-intro/01-print-numbers.cu -run